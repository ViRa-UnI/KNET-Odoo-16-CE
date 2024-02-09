# User Guide for KNET Payment Integration Module

## Table of Contents

1. Introduction
2. Installation
3. Configuration
4. Making Payments
5. Viewing Transactions
6. Troubleshooting
7. Contact Information

## 1. Introduction

Welcome to the KNET Payment Integration Module for Odoo Version 16 Community Edition. This guide will walk you through the steps to install, configure, and use the KNET Payment Integration Module to accept payments from your customers in Kuwait.

## 2. Installation

To install the KNET Payment Integration Module, follow the steps outlined in the `installation_guide.md` located in the `documentation` directory of the module.

## 3. Configuration

After installation, you need to configure the module with your KNET merchant credentials. Navigate to the KNET Configuration Form in the Odoo backend by going to:

`Accounting > Configuration > Payment Acquirers > KNET`

Fill in the required fields such as `merchant_id` and `secret_key`. You can also enable `sandbox_mode` for testing purposes.

## 4. Making Payments

Once the module is configured, customers can select KNET as a payment option during the checkout process. They will be redirected to the KNET payment page to complete the transaction.

## 5. Viewing Transactions

To view the transaction logs, access the Payment Transaction Dashboard by navigating to:

`Accounting > Payments > Payment Transactions`

Here you can filter and search for specific transactions using various criteria such as `transaction_id`, `payment_status`, and `transaction_date`.

## 6. Troubleshooting

If you encounter any issues with the KNET Payment Integration Module, please refer to the `troubleshooting` section in the `user_guide.md`. Ensure that all configurations are correct and that you have the latest version of the module.

## 7. Contact Information

For further assistance, please contact the module support team at support@example.com. Provide detailed information about the issue you are facing, including any error messages and screenshots if possible.

Thank you for using the KNET Payment Integration Module. We hope it enhances your Odoo experience by providing a seamless payment processing solution.