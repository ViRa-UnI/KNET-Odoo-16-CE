# KNET Payment Gateway Configuration Guide

## Introduction

This guide provides step-by-step instructions on how to configure the KNET Payment Integration Module for Odoo Version 16 Community Edition. By following this guide, administrators can set up the module to accept payments through the KNET payment gateway.

## Prerequisites

Before proceeding with the configuration, ensure that you have:

- Installed the KNET Payment Integration Module. Refer to `installation_guide.md` for installation instructions.
- Administrative access to your Odoo instance.

## Configuration Steps

### Step 1: Accessing the Configuration Menu

1. Log in to your Odoo instance with an administrator account.
2. Navigate to the **Settings** menu.
3. Under the **Payments** section, click on **Payment Acquirers**.

### Step 2: Setting Up KNET Payment Acquirer

1. In the Payment Acquirers list, find and select **KNET**.
2. You will be redirected to the KNET configuration form.

### Step 3: Configuring KNET Credentials

1. In the **KNET Configuration** section, fill in the following fields:
   - **Merchant ID**: Enter your KNET merchant ID.
   - **Secret Key**: Enter the secret key provided by KNET.
2. To test the integration before going live, toggle the **Sandbox Mode** to **True**.

### Step 4: Enabling the Payment Method

1. To enable KNET as a payment option, set the **State** field to **Enabled**.
2. Click on **Save** to apply the changes.

### Step 5: Customizing Payment Options (Optional)

1. Customize the payment page appearance by uploading a custom logo under the **Appearance** section.
2. Adjust the payment flow settings according to your preferences.

### Step 6: Testing the Configuration

1. If **Sandbox Mode** is enabled, perform a test transaction to ensure that the integration is working correctly.
2. Check the **Payment Transaction Dashboard** for the test transaction details.

### Step 7: Going Live

1. Once you have successfully tested the integration, disable **Sandbox Mode** by setting it to **False**.
2. Perform a live transaction to confirm that the module is correctly processing real payments.

## Troubleshooting

If you encounter any issues during configuration or testing, refer to the following:

- Ensure that all credentials are entered correctly without any leading or trailing spaces.
- Verify that your KNET account is active and properly set up to accept payments.
- Consult the `user_guide.md` for common issues and solutions.

## Conclusion

After completing these steps, your Odoo instance should be successfully integrated with the KNET payment gateway. For further assistance or advanced configurations, please refer to the official KNET documentation or contact KNET support.

Remember to periodically check for updates to the module to ensure compatibility and access to new features.