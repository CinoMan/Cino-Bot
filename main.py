import discord
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba, adım Cino-Bot! ben bir botum.')

@bot.command()
async def bilgi(ctx):
    await ctx.send(f'Merhaba! Ben de Cino-Bot. Ben CinoMan tarafından programlanmış bir botum. Benimle konuşabilir, selamlaşabilir, hatta resim belleği olarak bile kullanabilirsin.')

@bot.command()
async def selamunaleyküm(ctx):
    await ctx.send(f'Aleykümselam mümin kardeşim, adım Cino-Bot! ben bir botum.')

@bot.command()
async def ez(ctx):
    await ctx.send(f'Bez, gez, kez, tez enez, obez, üvez çepez, çerez, çömez, diyez, eğrez, falez, firez, güvez, kepez, melez, ortez, ölmez, pünez ançüez, çerkez, erimez, fernez, geçmez, görmez, körfez, menfez, merkez, müfrez, pekmez, protez, sentez, trapez anamnez, antitez, çekelez, çekemez, etyemez, göbelez, hipotez, mayonez, metatez, muazzez, polonez balyemez, benzemez, bilinmez, bölünmez, değişmez, epigenez, görünmez, hüryemez, kerkenez, manganez, mücehhez, parantez, tükenmez, varyemez, beklenmez, bilinemez, filogenez, güngörmez, haletinez, lebdeğmez, ontogenez, renksemez fotosentez, hıdırellez, interkinez, karyokinez, sugötürmez değerbilmez, dudakdeğmez, kadirbilmez, kargasekmez, sözgötürmez antrparantez, iyilikbilmez, karıncaezmez, partenogenez, sözünübilmez kurşungeçirmez, karıncaincitmez.')

@bot.command()
async def walterwhite(ctx):
    await ctx.send(f'https://tenor.com/view/wink-walt-cocky-breaking-bad-walter-white-gif-15121565')

@bot.command()
async def haha(ctx, count_haha = 5):
    await ctx.send("ha" * count_haha)

@bot.command()
async def kaydet(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename 
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send("Dosyanı kaydettim")
    else:
        await ctx.send(f'Beni mi deniyon, nerede fotoğraf')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url 
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{file_name}"))

    else:
        await ctx.send("Maalesef ekte bir dosya yok")

def get_class(model_path, labels_path ,image_path):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(model_path, compile=False)

    # Load the labels
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("/content/test.jpg").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")

bot.run("MTE1OTg5NDM0NDEzMjczNTAwNg.GNFRXc.5LRR2pOatz12K9PdSWTKi6N40_PFG1YIR5PWUU")