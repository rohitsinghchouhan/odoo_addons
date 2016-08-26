{
    'name': "Hotel Management",
    'version': '1.0',
   
    'author': "Digital Marketing",
    'category': 'Test',
    'description': """
    Simple module to show daily hotel information exchange. Update on daily base.
    """,

     'depends': ['base','website'],

     
    # data files always loaded at installation
    'data': [
        'data/hotelmanagement_data.xml',
        'views/customer_views.xml',        
        'views/views_menu.xml',
        'views/room_views.xml',
        'views/regst_views.xml',
        'views/workflow_views.xml',
        'views/partners_views.xml',
        'views/temp_demo_views.xml',
        'views/temp_home_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo_data.xml',
    # ],
}