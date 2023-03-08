from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
import qrcode

# Create your models here.
class Write (models.Model):
    name=models.CharField(max_length=200)
    qr_code=models.ImageField(upload_to='qr_code',blank=True)


    def __str__(self):
        return str(self.name)
    
    def save(self,*args,**kwargs):
        
        qrcode_image=qrcode.make(self.name)
        canvas=Image.new('RGB',(290,290),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        fname=f'qr_code-{self.name}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)
