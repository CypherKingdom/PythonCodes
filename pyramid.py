# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. 
# The pyramid is stacked according to one simple principle: each lower layer contains 
# one block more than the layer above. 
# Your task is to write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.

# Note: the height is measured by the number of fully completed layers – if the builders 
# don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

def pyramid_height(blocks):
    height, i=0, 1
    while i<=blocks:
        blocks-=i
        height+=1
        i+=1
    return height
blocks = int(input("Enter the number of blocks: "))
print("The height of the pyramid is:" + str(pyramid_height(blocks)))