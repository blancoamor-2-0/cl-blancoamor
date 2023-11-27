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
    'external_dependencies': {'python': ['twilio', 'html2text']},
    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',
    'config': [
        'db_name = odoo',
        'list_db = False',
        'dbfilter = odoo',
    ],

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8016',
    'longpolling_port': '8078',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'git@github.com:blancoamor-2-0/cl-blancoamor.git',
        'git@github.com:blancoamor-2-0/ba_sales.git blancoamor/ba_sales',
        'git@github.com:blancoamor-2-0/ba_base.git blancoamor/ba_base',
        'git@github.com:blancoamor-2-0/ba_delivery_zone.git blancoamor/ba_delivery_zone',
        'git@github.com:blancoamor-2-0/ba_product.git blancoamor/ba_product',
        'git@github.com:blancoamor-2-0/ba_purchase.git blancoamor/ba_purchase',
        'git@github.com:blancoamor-2-0/ba_website.git blancoamor/ba_website',
        'git@github.com:blancoamor-2-0/ba_hr.git blancoamor/ba_hr',

        # 'git@code.gestionblancoamor.com:odoo-13/ba_campus.git blancoamor/ba_hr',
        'git@github.com:blancoamor-2-0/ba_campus.git blancoamor/ba_campus',
        # 'git@code.gestionblancoamor.com:filoquin/website_themes.git varios/website_themes',
        'git@github.com:blancoamor-2-0/website_themes.git varios/website_themes',
        # 'git@code.gestionblancoamor.com:filoquin/ux.git varios/ba-ux',
        'git@github.com:blancoamor-2-0/ba_ux.git varios/ba-ux',
        'git@code.gestionblancoamor.com:odoo-13/ks_dashboard_ninja.git varios/ks_dashboard_ninja',

        # mercado pago
        'https://github.com/plugberry/mercadopago.git -b 13.0 varios/mercadopago',
        
        'https://github.com/filoquin/account_debt_management.git varios/account-debt-management',
        'https://github.com/ingadhoc/account-analytic.git adhoc/account-analytic',
        'https://github.com/ingadhoc/account-invoicing.git adhoc/account-invoicing',
        'https://github.com/ingadhoc/argentina-sale.git adhoc/argentina-sale',
        'https://github.com/ingadhoc/multi-company.git adhoc/multi-company',
        'https://github.com/ingadhoc/odoo-argentina.git adhoc/odoo-argentina',
        'https://github.com/ingadhoc/product.git adhoc/product',
        'https://github.com/ingadhoc/purchase.git adhoc/purchase',
        'https://github.com/ingadhoc/stock.git adhoc/stock',
        'https://github.com/ingadhoc/account-financial-tools.git adhoc/account-financial-tools',
        'https://github.com/ingadhoc/account-payment.git adhoc/account-payment',
        'https://github.com/ingadhoc/miscellaneous.git adhoc/miscellaneous',
        'https://github.com/ingadhoc/multi-store.git adhoc/multi-store',
        'https://github.com/ingadhoc/project.git adhoc/project',
        'https://github.com/ingadhoc/sale.git adhoc/sale ',
        'https://github.com/ingadhoc/website.git adhoc/website',
        'https://github.com/hormigaG/odoo-argentina-ce.git -b 13.0_BA adhoc/odoo-argentina-ce',
        'https://github.com/OCA/account-analytic.git oca/account-analytic',
        'https://github.com/OCA/crm.git oca/crm',
        'https://github.com/OCA/hr-expense.git oca/hr-expense',
        'https://github.com/OCA/management-system.git oca/management-system',
        'https://github.com/OCA/project.git oca/project',
        'https://github.com/OCA/sale-financial.git oca/sale-financial',
        'https://github.com/OCA/server-ux.git oca/server-ux',
        'https://github.com/OCA/web.git oca/web',
        'https://github.com/OCA/website.git oca/website',
        'https://github.com/OCA/account-financial-reporting.git oca/account-financial-reporting',
        'https://github.com/OCA/geospatial.git oca/geospatial',
        'https://github.com/OCA/hr-holidays.git oca/hr-holidays',
        'https://github.com/OCA/partner-contact.git oca/partner-contact',
        'https://github.com/OCA/purchase-workflow.git oca/purchase-workflow',
        'https://github.com/OCA/sale-workflow.git oca/sale-workflow',
        'https://github.com/OCA/social.git oca/social',
        'https://github.com/OCA/wms.git oca/wms',
        'https://github.com/OCA/account-financial-tools.git oca/account-financial-tools',
        'https://github.com/OCA/hr.git oca/hr',
        'https://github.com/OCA/knowledge.git oca/knowledge',
        'https://github.com/OCA/product-attribute.git oca/product-attribute',
        'https://github.com/OCA/queue.git oca/queue',
        'https://github.com/OCA/server-brand.git oca/server-brand',
        'https://github.com/OCA/stock-logistics-warehouse.git oca/stock-logistics-warehouse',
        'https://github.com/OCA/brand.git oca/brand',
        'https://github.com/OCA/hr-attendance.git oca/hr-attendance',
        'https://github.com/OCA/maintenance.git oca/maintenance',
        'https://github.com/OCA/product-pack.git oca/product-pack',
        'https://github.com/OCA/reporting-engine.git oca/reporting-engine',
        'https://github.com/OCA/server-tools.git oca/server-tools',
        'https://github.com/OCA/stock-logistics-workflow.git oca/stock-logistics-workflow',
        'https://github.com/OCA/contract.git oca/contract',
        'https://github.com/OCA/bank-statement-import.git oca/bank-statement-import',
        'https://github.com/OCA/server-backend.git oca/server-backend',
        'https://github.com/OCA/account-invoicing/ oca/account-invoicing',
        'https://github.com/OCA/payroll.git oca/payroll',
        'https://github.com/OCA/e-commerce.git oca/e-commerce',
        'https://github.com/OCA/delivery-carrier.git oca/delivery-carrier',
        'https://github.com/odoomates/odooapps varios/odooapps',

        # 'git@code.gestionblancoamor.com:odoo-13/blancoamor.git'

    ],
    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        # 'postgres postgres:10.1-alpine',
        'postgres mdillon/postgis:11-alpine',
        #'nginx nginx'
    ]
    # 'base_dir': '/opt/odoo/docker_files/'
}
