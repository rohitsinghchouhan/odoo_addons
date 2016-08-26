{
    'name': "Openacademy",
    'version': '1.0',
    'depends': ['base'],
    'author': "Digital Marketing",
    'category': 'Test',
    'description': """
    Simple module to show daily educational information exchange. Update on daily base.
    """,
    # data files always loaded at installation
    'data': [
        'data/openacademy_data.xml',
        'views/views.xml',
        'views/session_views.xml',
        'views/instructor_views.xml'
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo_data.xml',
    # ],
}