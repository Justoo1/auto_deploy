{
    'name': 'AUTO DEPLOYMENT',
    'version': '16.0.1.0.0',
    'summary': """ Testing auto deployment. """,
    'description': """ deployment testing""",
    'category': 'manufacture',
    'author': 'Justice Amankrah',
    'company': 'OakTech',
    'maintainer': 'Justice Amankrah',
    'depends': ['base'],
    'website': 'https://oaktech.com',
    'data': [
        'security/ir.model.access.csv',
        # 'security/deploy_security.xml',
        'views/deploy_views.xml',
    ],
    'images': [''],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
