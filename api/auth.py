from typing import Any
from django.http import HttpRequest
from ninja.security.apikey import APIKeyCookie


class SellerAuthentication(APIKeyCookie):
    def authenticate(self, request: HttpRequest, key: str | None) -> Any | None:
        if request.user.is_authenticated and request.user.is_seller:
            return request.user
        return None
