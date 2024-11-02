from encryption_service.encryptor import Encryptor
from encryption_service.key_manager import KeyManager
import encryption_service.config as config

def main():
    # Generate salt and key
    salt = KeyManager.generate_salt()
    key = KeyManager.generate_key(config.PASSWORD, salt)

    # Create an Encryptor instance
    encryptor = Encryptor(key)

    # Example data (credit card number)
    credit_card_number = "4111111111111111"

    # Encrypt the credit card number
    encrypted_data = encryptor.encrypt(credit_card_number)
    print("Encrypted Data:", encrypted_data)

    # Decrypt the data
    decrypted_data = encryptor.decrypt(encrypted_data)
    print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
        