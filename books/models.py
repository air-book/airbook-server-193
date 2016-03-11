import os
from django.db import models
#from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
#from django.contrib.auth.models import User
from authtools.models import User
from jsonfield import JSONField






class BookCategory(models.Model):
    tags = models.CharField(max_length=16, help_text="Aggiungere massimo 3 Tags")
    #order = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ['order']


    def __unicode__(self):
        return u'%s-%s' %(self.tags, self.order)

#class BookShopUserInline(admin.TabularInline):
#    classes = ('grp-collapse grp-open',)
#    model = Allegatoistanza
#    extra = 0


class BookShop(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(BookCategory)
    def _tipologie(self):
        return (', '.join([u'{}'.format(x) for x in self.tags.all().values_list('tags',flat=True)]))
    tipologie = property(_tipologie)


    def __unicode__(self):
        return u'%s' % self.name

class BookShopUser(models.Model):
    user = models.OneToOneField(User)
    bookshop = models.ForeignKey(BookShop)

    def __unicode__(self):
        return u'%s' % self.user


class BookAuthor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s' %(self.name)


class BookCategoryType(models.Model):
    CATEGORY_TYPE = (
    ('PRIMA EDIZIONE', 'Prima Edizione'),
    ('EDIZIONE ECONOMICA', 'Edizione Economica'),
    ('LIBRO ANTICO', 'Libro Antico 400'),
    ('LIBRO ANTICO', 'Libro Antico 500'),
    ('LIBRO ANTICO', 'Libro Antico 600'),
    ('LIBRO ANTICO', 'Libro Antico 700'),
    ('LIBRO ANTICO', 'Libro Antico 800'),
    ('LIBRO AUTOGRAFATO', 'Libro Autografato'),
    ('LIBRO D'' ARTISTA', 'Libro d'' Artista'),
    )
    #type = models.CharField(max_length=30, choices=CATEGORY_TYPE, null=True, blank=True)
    category_type = models.CharField(max_length=30, choices=CATEGORY_TYPE, null=True, blank=True)
    type = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="category_type_image")

    def __unicode__(self):
        return u'%s' %(self.category_type)

class BookEditor(models.Model):
    editor = models.CharField(max_length=500)
    nationality = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return u'%s' % self.editor

class CoverMaterial(models.Model):
    material = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.material

class CoverBack(models.Model):
    back = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.back

class CoverRilegatura(models.Model):
    rilegatura = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.rilegatura

class CoverImposition(models.Model):
    imposition = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.imposition


BOOK_CONDITIONS = (
    (0, 'Pessimo'),
    (1, 'Medio'),
    (2, 'Buono'),
    (3, 'Ottimo'),
    (4, 'Nuovo'),
)


COVER_TYPE = (
    ('COPERTINA MORBIDA', 'Copertina Morbida'),
    ('COPERTINA RIGIDA', 'Copertina Rigida'),
    ('COPERTINA RIGIDA CON SOVRACOPERTA', 'Copertina Rigida con Sovracoperta'),
    ('ALTRO', 'Altro'),
)

VOLUMES_TYPE = (
    (0, 'Raccolta di n volumi'),
    (1, 'Volume Singolo'),
)


class Book(models.Model):
    bookshop = models.ForeignKey(BookShop)
    title_art = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    def _title_complete(self):
        return '%s %s'%(self.title_art, self.title) 
    title_complete = property(_title_complete)    
    subtitle = models.CharField(max_length=500)
    authors = models.ManyToManyField(BookAuthor)
    editor = models.ForeignKey(BookEditor)
    volumes_type = models.IntegerField(choices=VOLUMES_TYPE)
    volumi_raccolta = models.IntegerField(null=True, blank=True, help_text='Numero totale dei volumi che compongono la raccolta')
    numero_volume_della_raccolta = models.IntegerField(null=True, blank=True, help_text='Numero del volumi all''interno della raccolta')
    conditions = models.IntegerField(choices=BOOK_CONDITIONS, null=True, blank=True)
    conditions_detail = JSONField(null=True, blank=True)    
    price = models.FloatField(null=True, blank=True)
    cover = models.CharField(max_length=20, choices=COVER_TYPE, null=True, blank=True)
    box = models.BooleanField(default=False)
    cover_material = models.ForeignKey(CoverMaterial, null=True, blank=True)
    back = models.ForeignKey(CoverBack)
    rilegatura = models.ForeignKey(CoverRilegatura)
    imposition = models.ForeignKey(CoverImposition)
    page_number = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    weigth = models.IntegerField(null=True, blank=True)
    heigth = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=2000)
    language = models.CharField(max_length=20, null=True, blank=True)    
    archive_code = models.CharField(max_length=10, null=True, blank=True)
    tags = models.ManyToManyField(BookCategory)
    isbn_code_10 = models.CharField(max_length=10, null=True, blank=True)
    isbn_code_13 = models.CharField(max_length=13, null=True, blank=True)
    category_type = models.ManyToManyField(BookCategoryType)
    saleable = models.BooleanField(default=False)
    publish = models.BooleanField(default=True)
    note = models.CharField(max_length=1000, null=True, blank=True)
    altri_canali = models.CharField(max_length=1000, null=True, blank=True)


    def __unicode__(self):
        return u'%s' % self.title


    def save(self, *args, **kwargs):
        if self.price and self.editor:
            self.saleable = True
        else:
            self.saleable = False


        return super(Book, self).save(*args, **kwargs)


class BookImage(models.Model):
    book = models.ForeignKey(Book, related_name="images")
    image = models.ImageField(upload_to="book_images")
    order = models.IntegerField(null=True, blank=True, default=0)
    image_thumb = ImageSpecField(source='image',
                                      processors=[ResizeToFill(400, 250)],
                                      format='JPEG',
                                      options={'quality': 90})

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % os.path.basename(self.image.path)
