@api_view(['GET'])
def instructions_data(request):
    """
    API endpoint для данных инструкций для студентов.
    Возвращает пошаговые руководства по важным процедурам из базы данных.
    """
    try:
        # Получаем все активные инструкции из базы данных
        guides = StudentGuide.objects.filter(is_active=True).prefetch_related(
            'requirements', 'steps__details'
        ).order_by('order')
        
        # Сериализуем данные
        serializer = StudentGuideSerializer(guides, many=True, context={'request': request})
        
        # Преобразуем данные в формат, ожидаемый фронтендом
        student_guides = []
        for guide_data in serializer.data:
            # Преобразуем требования в простой список строк для каждого языка
            requirements_ru = [req['text_ru'] for req in guide_data.get('requirements', [])]
            requirements_kg = [req['text_kg'] for req in guide_data.get('requirements', [])]
            requirements_en = [req['text_en'] for req in guide_data.get('requirements', [])]
            
            # Преобразуем шаги в нужный формат
            steps = []
            for step_data in guide_data.get('steps', []):
                # Преобразуем детали шага в простой список строк для каждого языка
                details_ru = [detail['text_ru'] for detail in step_data.get('details', [])]
                details_kg = [detail['text_kg'] for detail in step_data.get('details', [])]
                details_en = [detail['text_en'] for detail in step_data.get('details', [])]
                
                step = {
                    "step_number": step_data.get('step_number', 1),
                    "title_ru": step_data.get('title_ru', ''),
                    "title_kg": step_data.get('title_kg', ''),
                    "title_en": step_data.get('title_en', ''),
                    "description_ru": step_data.get('description_ru', ''),
                    "description_kg": step_data.get('description_kg', ''),
                    "description_en": step_data.get('description_en', ''),
                    "timeframe_ru": step_data.get('timeframe_ru', ''),
                    "timeframe_kg": step_data.get('timeframe_kg', ''),
                    "timeframe_en": step_data.get('timeframe_en', ''),
                    "details_ru": details_ru,
                    "details_kg": details_kg,
                    "details_en": details_en
                }
                steps.append(step)
            
            # Формируем данные инструкции в ожидаемом формате
            guide = {
                "id": guide_data['id'],
                "title_ru": guide_data.get('title_ru', ''),
                "title_kg": guide_data.get('title_kg', ''),
                "title_en": guide_data.get('title_en', ''),
                "description_ru": guide_data.get('description_ru', ''),
                "description_kg": guide_data.get('description_kg', ''),
                "description_en": guide_data.get('description_en', ''),
                "icon": guide_data.get('icon', 'DocumentTextIcon'),
                "estimated_time_ru": guide_data.get('estimated_time_ru', ''),
                "estimated_time_kg": guide_data.get('estimated_time_kg', ''),
                "estimated_time_en": guide_data.get('estimated_time_en', ''),
                "max_duration_ru": guide_data.get('max_duration_ru', ''),
                "max_duration_kg": guide_data.get('max_duration_kg', ''),
                "max_duration_en": guide_data.get('max_duration_en', ''),
                "contact_info_ru": guide_data.get('contact_info_ru', ''),
                "contact_info_kg": guide_data.get('contact_info_kg', ''),
                "contact_info_en": guide_data.get('contact_info_en', ''),
                "category": guide_data.get('category', 'academic'),
                "requirements_ru": requirements_ru,
                "requirements_kg": requirements_kg,
                "requirements_en": requirements_en,
                "steps": steps
            }
            student_guides.append(guide)
        
        response_data = {
            "student_guides": student_guides
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {"error": f"Ошибка получения данных инструкций: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
