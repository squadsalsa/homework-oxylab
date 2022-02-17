# Run latest debian image
```docker run -it --cap-add=NET_ADMIN --rm -v ${PWD}:/app debian /bin/bash```

# Prepare container for use, install ansible
```
cd /app
bash scripts/bootstrap.sh
```

# Run ansible playbook
```ansible-playbook rabbitmq.yaml -i inventory --vault-password-file .vault_pass```