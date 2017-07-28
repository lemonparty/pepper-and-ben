function createConfig(params) {
	const isProduction = params.isProduction;
	const min = isProduction ? ".min" : "";
	const webpack = require("webpack");
	const ExtractTextPlugin = require("extract-text-webpack-plugin");
	const WebpackNotifierPlugin = require("webpack-notifier");


	// settings common to both `watch` and `build`
	// --------------------------------------------------------------------------

	const entry = {
		app: "./src/app.js",
	};

	const output = {
		path: __dirname + "/../static",
		filename: `[name]${min}.js`,
		publicPath: "./",
	};

	const resolve = {
		extensions: [".webpack.js", ".web.js", ".js", ".jsx", ".scss", ".sass"]
	};

	const module = {
		loaders: [
			// sass: pull into standalone file
			{
				test: /\.(sass|scss)$/,
				exclude: [/node_modules/],
				loader: ExtractTextPlugin.extract("css-loader!sass-loader")
			},
		]
	};

	plugins = [
		new ExtractTextPlugin(`app${min}.css`, {
			allChunks: true
		}),
		new WebpackNotifierPlugin(),
	];


	// production options
	// --------------------------------------------------------------------------

	if (isProduction) {
		plugins.push(
			new webpack.DefinePlugin({
				"process.env": {
					NODE_ENV: JSON.stringify("production")
				}
			})
		);

		plugins.push(
			new webpack.optimize.UglifyJsPlugin({
				compress: {
					warnings: false,
				},
			})
		);
	}


	// the config object
	// --------------------------------------------------------------------------

	return {
		entry,
		output,
		resolve,
		module,
		plugins,
	};
}

module.exports = createConfig;
