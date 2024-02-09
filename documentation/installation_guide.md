# KNET Payment Integration Module Installation Guide

## Prerequisites
Before you begin the installation, make sure you have the following:
- Access to an Odoo Version 16 Community Edition instance with administrative privileges.
- The module files downloaded from the source repository.

## Installation Steps

1. **Upload the Module:**
   - Navigate to the Odoo server directory where third-party modules are stored, typically under `/addons`.
   - Upload the entire folder containing the KNET Payment Integration Module to this directory.

2. **Update Module List:**
   - Log in to your Odoo instance with administrative rights.
   - Navigate to `Apps` and click on `Update Apps List`. You may need to remove the `Apps` filter to see this option.

3. **Install the Module:**
   - In the Apps menu, search for `KNET Payment Integration`.
   - Click on the `Install` button next to the module.

4. **Configure File Permissions:**
   - Ensure that the Odoo server has read and write permissions for the newly uploaded module files.
   - You can set the appropriate permissions using the command `chmod` or through your server's file management interface.

5. **Restart Odoo Service:**
   - Depending on your hosting setup, restart the Odoo service to apply the changes. This can typically be done using a command like `service odoo restart` or through your hosting provider's control panel.

6. **Verify Installation:**
   - Once the Odoo service is back up, log in to the Odoo instance.
   - Go to `Apps` and remove the `Apps` filter. You should see the `KNET Payment Integration` module listed as installed.

## Post-Installation Steps

1. **Configure Payment Acquirer:**
   - Navigate to `Invoicing` > `Configuration` > `Payment Acquirers`.
   - Find `KNET` in the list of payment acquirers and click `Configure`.
   - Enter your KNET merchant details and other settings as required.

2. **Set Up Security Groups:**
   - Import the security group definitions from the `security/ir.model.access.csv` file to define access rights for different user roles.

3. **Load Initial Data:**
   - If provided, load initial data from the `data/payment_acquirer_data.xml` file to pre-populate necessary records.

4. **Test the Integration:**
   - Follow the testing procedures outlined in the `tests/test_integration.py` file to ensure the module is functioning correctly.

## Troubleshooting

If you encounter any issues during installation, please refer to the `documentation/user_guide.md` and `documentation/configuration_guide.md` for guidance. For further assistance, contact the module support team or refer to the Odoo community forums.

Congratulations! You have successfully installed the KNET Payment Integration Module for Odoo Version 16 Community Edition.