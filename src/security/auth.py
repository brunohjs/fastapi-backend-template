import fastapi


def get_current_user(token: str):
    # Aqui você implementaria a lógica de validação do token e recuperação do usuário
    user = None  # Exemplo simplificado
    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    return user
