# ФАЙЛ ВРЕМЕННО ОТКЛЮЧЕН - ИСПОЛЬЗУЮТСЯ РУЧНЫЕ ПОЛЯ ПЕРЕВОДОВ
# from modeltranslation.translator import translator, TranslationOptions
# from .models import MissionSection, HistoryMilestone, Value, Priority, Achievement


# class MissionSectionTranslationOptions(TranslationOptions):
#     """
#     Настройка перевода для модели MissionSection
#     """
#     fields = (
#         'title', 'subtitle', 'mission_text',
#         'vision_title', 'vision_text', 
#         'approach_title', 'approach_text',
#         'achievements_subtitle', 'impact_title', 'impact_text',
#         'future_title', 'future_text'
#     )


# class HistoryMilestoneTranslationOptions(TranslationOptions):
#     """
#     Настройка перевода для модели HistoryMilestone
#     """
#     fields = ('title', 'description')


# class ValueTranslationOptions(TranslationOptions):
#     """
#     Настройка перевода для модели Value
#     """
#     fields = ('title', 'description')


# class PriorityTranslationOptions(TranslationOptions):
#     """
#     Настройка перевода для модели Priority
#     """
#     fields = ('text',)


# class AchievementTranslationOptions(TranslationOptions):
#     """
#     Настройка перевода для модели Achievement
#     """
#     fields = ('label',)


# # Регистрация моделей для перевода
# translator.register(MissionSection, MissionSectionTranslationOptions)
# translator.register(HistoryMilestone, HistoryMilestoneTranslationOptions)
# translator.register(Value, ValueTranslationOptions)
# translator.register(Priority, PriorityTranslationOptions)
# translator.register(Achievement, AchievementTranslationOptions)