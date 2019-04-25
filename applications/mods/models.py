from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('name', max_length=15)
    code = models.CharField('code', max_length=2)

    def __str__(self):
        return self.code


class Mod(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250, blank=True)
    url = models.SlugField(allow_unicode=True, blank=True)
    title_image = models.ImageField(blank=True, upload_to='mod/title_image/')
    rating = models.SmallIntegerField(blank=True)

    tag = models.ManyToManyField(Tag, blank=True)
    compatibility_mod = models.ManyToManyField('Mod', blank=True, related_name='mod_compatibilities')
    incompatibility_mod = models.ManyToManyField('Mod', blank=True, related_name='mod_incompatibilities')

    description = models.TextField(max_length=2000, blank=True)

    order_index = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )
        default_related_name = 'mods'

    def __str__(self):
        return self.name


class ModFile(models.Model):
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE, related_name='mod_files')
    file = models.FileField(upload_to='mod/files')
    description = models.TextField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('mod', )

    def __str__(self):
        return '%s %s' % (self.mod, self.file)


class ModImage(models.Model):
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE, related_name='mod_images')
    image = models.ImageField(upload_to='mod/images')
    description = models.TextField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('mod',)

    def __str__(self):
        return '%s %s' % (self.mod, self.image)
