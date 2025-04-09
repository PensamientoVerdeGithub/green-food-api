from app import create_app

app = create_app()

if __name__ == '__main__':
  print('Green Food API')
  app.run(port=5000)
