# Exemple minimal de chat completion Mistral

Premier appel à l'API Chat Completion de Mistral avec le SDK officiel Python (`mistralai`), modèle `mistral-small-latest`.

## 1. Installer le SDK officiel

```bash
pip install mistralai
```

## 2. Générer une clé API dans Mistral Studio

1. Connectez-vous à [Mistral Studio](https://console.mistral.ai) (créez un compte si nécessaire).
2. Ouvrez la section **API Keys** de votre workspace.
3. Cliquez sur **New key**, renseignez un nom (ex. `quickstart`) et une date d'expiration.
4. Copiez la clé immédiatement : elle n'est affichée qu'une seule fois.

Quickstart officiel : [Activate Studio and generate an API key](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key).

## 3. Définir MISTRAL_API_KEY dans le terminal

Linux / macOS :

```bash
export MISTRAL_API_KEY="votre-cle-api"
```

Windows (PowerShell) :

```powershell
$env:MISTRAL_API_KEY="votre-cle-api"
```

## 4. Exécuter l'exemple

Depuis le dossier du projet :

```bash
python main.py
```

Documentation : [Chat completions](https://docs.mistral.ai/inference/conversations/chat-completion).
