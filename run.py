from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Cria as tabelas automaticamente se não existirem
        db.create_all()
    
    # Inicia o servidor local com hot-reload ativo
    app.run(debug=True)
