#!/bin/bash

# Check if terraform is installed
if ! command -v terraform &> /dev/null; then
    echo "Terraform is not installed. Please install it before running this script."
    exit 1
fi

cd "$(dirname "$0")"  # Change to the directory where the script is located

# Define the path to the .tfvars file
TFVARS_FILE="global.tfvars"

if [[ -z "$terraformclientid" || -z "$azuretenent" || -z "$azuresubscriptionid" || -z "$terraformazuresercet" ]]; then
    echo "One or more required environment variables are not set:"
    echo "  terraformclientid, azuretenent, azuresubscriptionid, terraformazuresercet"
    exit 1
fi


# Generate the .tfvars file from environment variables
echo "Generating $TFVARS_FILE from environment variables..."
{
    echo "client_id = \"${terraformclientid}\""
    echo "tenant_id = \"${azuretenent}\""
    echo "subscription_id = \"${azuresubscriptionid}\""
    echo "client_secret = \"${terraformazuresercet}\""
} > "$TFVARS_FILE"

echo "$TFVARS_FILE generated successfully."

# Initialize Terraform
echo "Initializing Terraform..."
terraform init

# Validate Terraform configuration
echo "Validating Terraform configuration..."
if ! terraform validate; then
    echo "Terraform validation failed. Please check your configuration."
    rm "$TFVARS_FILE"  
    exit 1
fi


# Plan Terraform deployment
echo "Planning Terraform deployment..."
if ! terraform plan -var-file="$TFVARS_FILE"; then
    echo "Terraform plan failed. Please check your configuration."
    rm "$TFVARS_FILE"  
    exit 1
fi
# Apply Terraform deployment

echo "Applying Terraform deployment..."
if ! terraform apply -var-file="$TFVARS_FILE" -auto-approve; then
    echo "Terraform apply failed. Please check your configuration."
    exit 1
fi
echo "Terraform build completed successfully."
rm "$TFVARS_FILE"  