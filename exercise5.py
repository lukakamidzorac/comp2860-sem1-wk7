class VigenereCipher:
    """
       VigenereCipher class.

       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        """
        Private method to shift a letter a number of positions forward or backward in the alphabet.

        Parameters
        ----------
        letter : str
            The letter to be shifted.
        shift: int
            The number to shift
        forward : bool
            Whether to shift forward (True) or backward (False).

        Returns
        -------
        str
            The shifted letter.
        """
        if not forward:
            shift = -shift
        position = ord(letter) - VigenereCipher.offset
        shifted_letter = chr((position + shift) % 26 + VigenereCipher.offset)
        return shifted_letter

    def __generate_shift_list(self, plaintext_length: int):
        """
        Private method to generate a list of integers. Each element is the shift to encrypt the
        plaintext letter at the same position.

        Parameters
        ----------
        plaintext_length : int
            The length of the plaintext after whitespace and punctuation has been removed.

        Returns
        -------
        list
            A list of shifts (integers).
        """
        shift_list = []
        for i in range(plaintext_length):
            key_letter = self.keyword[i % len(self.keyword)]
            shift_list.append(ord(key_letter) - VigenereCipher.offset)
        return shift_list

    def encrypt(self, plaintext: str):
        """
        Encrypts a plaintext string.

        Parameters
        ----------
        plaintext : str
            The plaintext string.

        Returns
        -------
        str
            The ciphertext string.
        """
        letters = ''.join(c for c in plaintext.upper() if c.isalpha())
        shift_list = self.__generate_shift_list(len(letters))
        ciphertext = ''
        for i in range(len(letters)):
            ciphertext += self.__shift_letter(letters[i], shift_list[i], True)
        return ciphertext

    def decrypt(self, ciphertext: str):
        """
        Decrypts a ciphertext string

        Parameters
        ----------
        ciphertext : str
            The ciphertext string.

        Returns
        -------
        str
            The plaintext string.
        """
        letters = ''.join(c for c in ciphertext.upper() if c.isalpha())
        shift_list = self.__generate_shift_list(len(letters))
        plaintext = ''
        for i in range(len(letters)):
            plaintext += self.__shift_letter(letters[i], shift_list[i], False)
        return plaintext


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()
