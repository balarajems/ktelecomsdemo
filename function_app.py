# __init__.py

import azure.functions as func
from plugins.telecom_support import TelecomSupportPlugin
from plugins.network_monitor import NetworkMonitorPlugin
from plugins.customer_support import CustomerSupportPlugin

# Create a Singleton FunctionApp instance
app = func.FunctionApp()

# Instantiate the plugin classes
telecom_support_plugin = TelecomSupportPlugin()
network_monitor_plugin = NetworkMonitorPlugin()
customer_support_plugin = CustomerSupportPlugin()

@app.route(route="telecom/network_summary", auth_level=func.AuthLevel.ANONYMOUS)
def network_summary(req: func.HttpRequest) -> func.HttpResponse:
    """Route for TelecomSupportPlugin -> network_summary"""
    report_text = req.params.get("report_text")
    if not report_text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            report_text = req_body.get("report_text")

    if not report_text:
        return func.HttpResponse(
            "Please provide 'report_text' in the query string or request body.",
            status_code=400
        )
    
    # Call the plugin method
    result = telecom_support_plugin.network_summary(report_text)
    return func.HttpResponse(result, status_code=200)

@app.route(route="network/status", auth_level=func.AuthLevel.ANONYMOUS)
def network_status(req: func.HttpRequest) -> func.HttpResponse:
    """Route for NetworkMonitorPlugin -> network_status"""
    result = network_monitor_plugin.network_status()
    return func.HttpResponse(result, status_code=200)

@app.route(route="customer/sentiment_analysis", auth_level=func.AuthLevel.ANONYMOUS)
def sentiment_analysis(req: func.HttpRequest) -> func.HttpResponse:
    """Route for CustomerSupportPlugin -> sentiment_analysis"""
    message = req.params.get("message")
    if not message:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            message = req_body.get("message")

    if not message:
        return func.HttpResponse(
            "Please provide 'message' in the query string or request body.",
            status_code=400
        )
    
    # Call the plugin method
    result = customer_support_plugin.sentiment_analysis(message)
    return func.HttpResponse(result, status_code=200)
