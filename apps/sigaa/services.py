from django.core.exceptions import ObjectDoesNotExist

from apps.base.utils import encrypt_password
from apps.sig.models import SigUsuario, SigPessoa, SigServidor, SigDiscente, SigStatusDiscente


class SigService:

    def autentica_sig(self, usuario, senha) -> SigUsuario:
        try:
            senha = encrypt_password(senha)
            query_base = SigUsuario.objects.filter(login=usuario, senha=senha)
            if query_base.exists():
                return query_base.first()

            raise ObjectDoesNotExist("Credenciais inválidas na Plataforma SIG")
        except ObjectDoesNotExist as exception:
            raise exception
