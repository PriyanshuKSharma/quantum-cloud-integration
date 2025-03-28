output "azure_function_url" {
  value = azurerm_function_app.function.default_hostname
}
output "azure_storage_account" {
  value = azurerm_storage_account.storage.name
}
