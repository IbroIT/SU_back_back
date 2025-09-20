from modeltranslation.translator import register, TranslationOptions
from .models import MediaCategory, MediaOutlet, MediaArticle, MediaTag


@register(MediaCategory)
class MediaCategoryTranslationOptions(TranslationOptions):
    fields = ('name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en')


@register(MediaOutlet)
class MediaOutletTranslationOptions(TranslationOptions):
    fields = ('name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en')


@register(MediaArticle)
class MediaArticleTranslationOptions(TranslationOptions):
    fields = (
        'title_ru', 'title_kg', 'title_en',
        'description_ru', 'description_kg', 'description_en',
        'content_ru', 'content_kg', 'content_en',
        'author_ru', 'author_kg', 'author_en'
    )


@register(MediaTag)
class MediaTagTranslationOptions(TranslationOptions):
    fields = ('name_ru', 'name_kg', 'name_en')
