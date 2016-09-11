var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  context: __dirname,
  entry: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      './assets/js/index.jsx'
  ],

  output: {
      path: path.resolve('./assets/bundles/'),
      filename: '[name].js',
      publicPath: 'http://localhost:3000/assets/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      { 
        test: /\.jsx?$/, 
        exclude: /node_modules/, 
        loaders: ['react-hot', 'babel'],
      },
      { test: /\.json$/, loader: "json-loader"}
    ],
  },

  resolve: {
    modulesDirectories: [
      'node_modules', 
      'bower_components',
      path.resolve("/assets/js/")
    ],
    extensions: ['', '.js', '.jsx']
  }
}