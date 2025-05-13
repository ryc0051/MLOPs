terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.2"
    }
  }
}

provider "azurerm" {
  subscription_id = var.subscription_id
  client_id       = var.client_id
  tenant_id       = var.tenant_id
  client_secret   = var.client_secret
  features {}
}

resource "azurerm_resource_group" "kubernetesragroup" {
    name     = "kubernetes-rg"
    location = "australiaeast"
}

resource "azurerm_storage_account" "terraformstorage" {
    name                     = "rycterraformstorage"
    resource_group_name      = azurerm_resource_group.kubernetesragroup.name
    location                 = azurerm_resource_group.kubernetesragroup.location
    account_tier             = "Standard"
    account_replication_type = "LRS"
}