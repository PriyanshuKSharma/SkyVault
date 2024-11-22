const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'public'),
    },
    setupMiddlewares: (middlewares, devServer) => {
      // Custom middleware logic goes here
      if (!devServer) {
        throw new Error('webpack-dev-server is not defined');
      }

      // Example middleware
      devServer.app.get('/some/path', function (req, res) {
        res.json({ custom: 'response' });
      });

      return middlewares;
    },
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
};
