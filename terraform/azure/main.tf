provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "quantum-kmeans-rg"
  location = "East US"
}

resource "azurerm_storage_account" "storage" {
  name                     = "quantumkmeanssa"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "container" {
  name                  = "quantumdata"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

resource "azurerm_function_app" "function" {
  name                = "QuantumKMeansAzure"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  storage_account_name       = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key
  app_service_plan_id = azurerm_service_plan.plan.id
  os_type             = "linux"
  app_settings    = {
    "FUNCTIONS_WORKER_RUNTIME" = "python"
  }
  # zip_deploy_file = "azure_function.zip"
}

resource "azurerm_service_plan" "plan" {
  name                = "quantum-kmeans-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
}
