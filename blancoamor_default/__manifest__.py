{
    'name': 'dck_blancoamor',
    'version': '13.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto ba con geo",
    'author': 'Ing. Gabriela Rivero',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,
    'external_dependencies': {'python':['twilio']},
    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8016',
    'longpolling_port': '8078',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [


        'https://github.com/filoquin/cl-blancoamor.git',
        'git@code.gestionblancoamor.com:odoo-13/ba_sales.git -b13.0 ba-ba_sales',
        'git@code.gestionblancoamor.com:odoo-13/ba_base.git -b13.0 ba-ba_base',
        'git@code.gestionblancoamor.com:odoo-13/ba_delivery_zone.git -b13.0 ba-ba_delivery_zone',
        'git@code.gestionblancoamor.com:odoo-13/ba_product.git -b13.0 ba-ba_product',
        'git@code.gestionblancoamor.com:odoo-13/ba_purchase.git -b13.0 ba-ba_purchase',
        'git@code.gestionblancoamor.com:odoo-13/ba_website.git -b13.0 ba-ba_website',
        'git@code.gestionblancoamor.com:odoo-13/ba_campus -b13.0.git ba-ba_campus',
        'git@code.gestionblancoamor.com:filoquin/website_themes.git ba -b13.0 /varios/website_themes',
        'git@code.gestionblancoamor.com:filoquin/ux.git -b13.0 ba-ux',
        'git@code.gestionblancoamor.com:odoo-13/ks_dashboard_ninja.git ba -b13.0/varios/ks_dashboard_ninja',
        'git@code.gestionblancoamor.com:odoo-13/ba_hr -b13.0 ba-ba_hr',
        'https://github.com/ingadhoc/account-analytic.git -b 13.0 adhoc-account-analytic',
        'https://github.com/ingadhoc/account-invoicing.git -b 13.0 adhoc-account-invoicing',
        'https://github.com/ingadhoc/argentina-sale.git -b 13.0 adhoc-argentina-sale',
        'https://github.com/ingadhoc/multi-company.git -b 13.0 adhoc-multi-company',
        'https://github.com/ingadhoc/odoo-argentina.git -b 13.0 adhoc-odoo-argentina',
        'https://github.com/ingadhoc/product.git -b 13.adhoc-0 product',
        'https://github.com/ingadhoc/purchase.git -b 13.adhoc-0 purchase',
        'https://github.com/ingadhoc/stock.git -b 13.adhoc-0 stock',
        'https://github.com/ingadhoc/account-financial-tools.git -b 13.0 account-adhoc-financial-tools',
        'https://github.com/ingadhoc/account-payment.git -b 13.0 adhoc-account-payment',
        'https://github.com/ingadhoc/miscellaneous.git -b 13.adhoc-0 miscellaneous',
        'https://github.com/ingadhoc/multi-store.git -b 13.0 adhoc-multi-store',
        'https://github.com/ingadhoc/project.git -b 13.0 adhoc-project',
        'https://github.com/ingadhoc/sale.git adhoc-sale -b 13.0',
        'https://github.com/ingadhoc/website.git -b 13.adhoc-0 website',
        'https://github.com/hormigaG/odoo-argentina-ce.git -b 13.0_BA odoo-adhoc-argentina-ce',
        'https://github.com/OCA/account-analytic.git -b13.0 account-analytic',
        'https://github.com/OCA/crm.git -b13.0 crm',
        'https://github.com/OCA/hr-expense.git -b13.0 hr-expense',
        'https://github.com/OCA/management-system.git -b13.0 management-system',
        'https://github.com/OCA/project.git -b13.0 project',
        'https://github.com/OCA/sale-financial.git -b13.0 sale-financial',
        'https://github.com/OCA/server-ux.git -b13.0 server-ux',
        'https://github.com/OCA/web.git -b13.0 web',
        'https://github.com/OCA/account-financial-reporting.git -b13.0 account-financial-reporting',
        'https://github.com/OCA/geospatial.git -b13.0 geospatial',
        'https://github.com/OCA/hr-holidays.git -b13.0 hr-holidays',
        'https://github.com/OCA/partner-contact.git -b13.0 partner-contact',
        'https://github.com/OCA/purchase-workflow.git -b13.0 purchase-workflow',
        'https://github.com/OCA/sale-workflow.git -b13.0 sale-workflow',
        'https://github.com/OCA/social.git -b13.0 social',
        'https://github.com/OCA/wms.git -b13.0 wms',
        'https://github.com/OCA/account-financial-tools.git -b13.0 account-financial-tools',
        'https://github.com/OCA/hr.git -b13.0 hr',
        'https://github.com/OCA/knowledge.git -b13.0 knowledge',
        'https://github.com/OCA/product-attribute.git -b13.0 product-attribute',
        'https://github.com/OCA/queue.git -b13.0 queue',
        'https://github.com/OCA/server-brand.git -b13.0 server-brand',
        'https://github.com/OCA/stock-logistics-warehouse.git -b13.0 stock-logistics-warehouse',
        'https://github.com/OCA/brand.git -b13.0 brand',
        'https://github.com/OCA/hr-attendance.git -b13.0 hr-attendance',
        'https://github.com/OCA/maintenance.git -b13.0 maintenance',
        'https://github.com/OCA/product-pack.git -b13.0 product-pack',
        'https://github.com/OCA/reporting-engine.git -b13.0 reporting-engine',
        'https://github.com/OCA/server-tools.git -b13.0 server-tools',
        'https://github.com/OCA/stock-logistics-workflow.git -b13.0 stock-logistics-workflow',
        'https://github.com/OCA/contract.git -b13.0 contract',
        'https://github.com/OCA/bank-statement-import.git -b13.0 bank-statement-import',
        'https://github.com/OCA/server-backend.git -b13.0 server-backend',
        'https://github.com/OCA/account-invoicing/ -b13.0 account-invoicing',
        'https://github.com/OCA/payroll.git -b13.0 payroll',
        'https://github.com/OCA/e-commerce.git -b13.0 e-commerce',
        'https://github.com/OCA/delivery-carrier.git -b13.0 delivery-carrier',

        'git@code.gestionblancoamor.com:odoo-13/blancoamor.git'

    ],
    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        # 'postgres postgres:10.1-alpine',
        'postgres mdillon/postgis:11-alpine',
        #'nginx nginx'
    ]
    #'base_dir': '/opt/odoo/docker_files/'
}
