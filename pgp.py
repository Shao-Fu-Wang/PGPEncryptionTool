import pgpy
import os
import filetype


from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
from datetime import timedelta, datetime

class pgp_util():
    def make_key(self, name = 'dbs'):
        key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
        uid = pgpy.PGPUID.new(name)
        key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes = [HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers = [SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression = [CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed],
            key_expiration = timedelta(days=7))
        return key
        
    def export_key(self, key, name):
        private_key = str(key)
        public_key = str(key.pubkey)
        
        public_key_file = open(name+"_public_key"+datetime.now().strftime("_%H_%M_%S_")+".asc", "w")
        public_key_file.write(public_key)
        public_key_file.close()

        private_key_file = open(name+"_private_key"+datetime.now().strftime("_%H_%M_%S_")+".asc", "w")
        private_key_file.write(private_key)
        private_key_file.close()


    
    def encryptUtil(self, public_key, file_path):
        message = pgpy.PGPMessage.new(file_path, file=True)
        enc_message = public_key.encrypt(message)
        return str(enc_message)
    
    def decryptUtil(self, private_key, data):
        message = pgpy.PGPMessage.from_blob(data)
        dec_message = private_key.decrypt(message).message
        try:
            dec_message = bytes(dec_message, 'utf-8') # txt file
        except:
            dec_message = bytes(dec_message) # other
        return dec_message

    def encryptFile(self, target_path, public_key_path):
        encrypt_key, _ = pgpy.PGPKey.from_file(public_key_path)
        # file = open(target_path, "r")
        # data = file.read()
        exp_file = open(target_path.split(".")[0]+"_encrypted", "w")
        exp_file.write(self.encryptUtil(encrypt_key, target_path))
        
    def decryptFile(self, target_path, private_key_path):
        decrypt_key, _ = pgpy.PGPKey.from_file(private_key_path)
        file = open(target_path, "r")
        data = file.read()
        decryptedMsg = self.decryptUtil(decrypt_key, data)
        extension = filetype.guess_extension(decryptedMsg)
        if(extension == None):
            extension = "txt"
        output_path = '/'.join(target_path.split('/')[:-1])+"/"+target_path.split('/')[-1].split('.')[0]+"_decrypt."+extension
        exp_file = open(output_path, "wb")
        exp_file.write(decryptedMsg)
        print(extension)
