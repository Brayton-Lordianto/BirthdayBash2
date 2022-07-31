import deso
import os

SEED_HEX = os.environ['SEED_HEX']
PUBLIC_KEY = os.environ['PUBLIC_KEY']
desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)

# plan: creates an nft from an image unto the deso blockchain
def createNFT(postHashHex):
    desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
    result = (desoSocial.createNFTBid(NFTPostHashHex=postHashHex, serialNumber=1, bidAmountDeso=2).json())
    print(result)
    
# transfers the nft from an organizer to participants
def transferNFT(postHashHex, receiverPublicKey):
    result = (desoSocial.transferNFT(postHashHex, receiverPublicKey, serialNumber=1).json())
    print(result)
    
# these methods both get called after the image and recepient data is found. 