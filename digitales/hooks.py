app_name = "digitales"
app_title = "digitales"
app_publisher = "digitales"
app_description = "digitales"
app_icon = "icon-truck"
app_color = "#966D58"
app_email = "rohitw1991@gmail.com"
app_url = "google.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/digitales/css/digitales.css"
# app_include_js = "/assets/digitales/js/digitales.js"

# include js, css files in header of web template
# web_include_css = "/assets/digitales/css/digitales.css"
# web_include_js = "/assets/digitales/js/digitales.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

fixtures = ['Custom Field', 'Property Setter']
# Installation
# ------------

# before_install = "digitales.install.before_install"
# after_install = "digitales.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "digitales.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Sales Order": {
		# "on_update": "digitales.digitales.Api_methods.create_purchase_order",
		"on_submit": "digitales.digitales.Api_methods.create_purchase_order",
		"on_update_after_submit" : "digitales.digitales.Api_methods.on_update_after_submit_so_methods",
		"on_cancel": "digitales.digitales.Api_methods.delete_stock_assignment"
	},

	"Purchase Receipt": {
		"on_submit": "digitales.digitales.Api_methods.stock_assignment",
		"on_cancel": "digitales.digitales.Api_methods.stock_cancellation"
	},

	"Delivery Note": {
		"on_submit": "digitales.digitales.Api_methods.update_stock_assignment_log_on_submit",
		"validate": "digitales.digitales.Api_methods.validate_qty_on_submit",
		"on_cancel": "digitales.digitales.Api_methods.update_stock_assignment_log_on_cancel"
		
	}
	
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		#"digitales.digitales.custom_methods.GetItem"
		#"digitales.digitales.custom_methods.GetCustomer"
		#"digitales.digitales.custom_methods.GetOrders"
		# "digitales.digitales.custom_methods.check_APItime"
		"digitales.digitales.Api_methods.check_APItime"

	]
# 	"daily": [
# 		"digitales.tasks.daily"
# 	],
#	"hourly": [
		#"digitales.tasks.hourly"
		#"digitales.digitales.custom_methods.GetItem"
		#"digitales.digitales.custom_methods.GetCustomer"
#		"digitales.digitales.custom_methods.GetOrders"
#	]
# 	"weekly": [
# 		"digitales.tasks.weekly"
# 	]
# 	"monthly": [
# 		"digitales.tasks.monthly"
# 	]
 }

# Testing
# -------

# before_tests = "digitales.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "digitales.event.get_events"
# }

