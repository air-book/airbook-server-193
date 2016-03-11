from django.contrib import admin


from .models import BookShop, Book, BookCategory, BookAuthor, BookImage, BookShopUser, \
BookEditor, CoverMaterial, CoverBack, CoverRilegatura, CoverImposition, BookCategoryType

class BookCategoryTypeAdmin(admin.ModelAdmin):
    list_display = ['icon', 'caterory_type']
    ordering = ['caterory_type', ]
    #fieldsets = [("Categorie", { 'fields': ('category_type', 'icon',),   'classes': ('grp-collapse grp-open', ), }),]
    
admin.site.register(BookCategoryType, BookCategoryTypeAdmin)


class BookEditorAdmin(admin.ModelAdmin):
    ordering = ['editor', 'nationality', ]
    list_filter = ['nationality', ]
    list_display = ['editor', 'nationality', ]


admin.site.register(BookEditor, BookEditorAdmin)

class CoverMaterialAdmin(admin.ModelAdmin):
    ordering = ['material', ]

admin.site.register(CoverMaterial, CoverMaterialAdmin)


class CoverBackAdmin(admin.ModelAdmin):
    ordering = ['back', ]

admin.site.register(CoverBack, CoverBackAdmin)


class CoverRilegaturaAdmin(admin.ModelAdmin):
    ordering = ['rilegatura', ]

admin.site.register(CoverRilegatura, CoverRilegaturaAdmin)


class CoverImpositionAdmin(admin.ModelAdmin):
    ordering = ['imposition', ]

admin.site.register(CoverImposition, CoverImpositionAdmin)





class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['tags', ]
    ordering = ['tags', ]
    
admin.site.register(BookCategory, BookCategoryAdmin)


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality', ]
    ordering = ['name', ]
    
admin.site.register(BookAuthor, BookAuthorAdmin)

class BookShopUserInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    model = BookShopUser
    extra = 0

class BookShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'tipologie', ]
    ordering = ['name', ]
    filter_horizontal = ('tags', )
    inlines = ([BookShopUserInline])
admin.site.register(BookShop, BookShopAdmin)

class BookShopUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'bookshop', ]
    ordering = ['user', ]

admin.site.register(BookShopUser, BookShopUserAdmin)


admin.site.register(BookImage)

class BookImageInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    model = BookImage
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookshop', 'title_complete', 'editor', 'conditions', 'price', 'cover', 'saleable')
    list_filter = ['bookshop', 'editor', 'authors', 'volumes_type', 'conditions', 'cover', 'cover_material', 'box', 'back', 'rilegatura', 'imposition', ]
    fieldsets = [
                ("Libreria", { 'fields': ('bookshop', ('price', 'saleable'), ('isbn_code_10', 'isbn_code_13'), 'altri_canali'), 
                               'classes': ('grp-collapse grp-open', ), 
                                           }),
                ("Anagrafica", { 'fields': (('title_art', 'title',), 'subtitle', ('authors', ), ('editor', 'publish', 'language', ), 'description' ), 
                                 'classes': ('grp-collapse grp-open', ), 
                                           }),
                ("Tipologia", { 'fields': ('volumes_type', 'volumi_raccolta', 'numero_volume_della_raccolta', 'caterory_type', ), 
                                'classes': ('grp-collapse grp-open', ), 
                                           }),                
                ("Condizioni", { 'fields': ('conditions', 'conditions_detail', ('box', 'cover', 'cover_material'), ), 
                                 'classes': ('grp-collapse grp-open', ), 
                                           }),                
                ("Caratteristiche", { 'fields': ('page_number',  ('width', 'weigth', 'heigth'), ('back', 'rilegatura', 'imposition',), 'tags', ), 
                                 'classes': ('grp-collapse grp-open', ), 
                                           }),                
                ("Note", { 'fields': ('note', ), 
                                 'classes': ('grp-collapse grp-open', ), 
                                           }),                
    ]    
    filter_horizontal = ('authors', 'caterory_type', 'tags', )
    change_list_template = "admin/change_list_filter_sidebar.html"
    inlines = ([BookImageInline])
    search_fields = ['title', 'title_art', 'tags__tags']
admin.site.register(Book, BookAdmin)