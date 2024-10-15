# myapp/validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_email_domain(value):
    allowed_domains = ['carinawear.com',]  # Replace with your allowed domains
    domain = value.split('@')[1] if '@' in value else None
    if domain not in allowed_domains:
        raise ValidationError(
            'Please Register using company email address.'
            # _('Invalid domain. Please use an email address with the following domains: %(allowed_domains)s'),
            # params={'allowed_domains': ', '.join(allowed_domains)},
        )
