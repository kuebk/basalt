## basalt

A fast, simple BSON parser for Node, available as an addon or as a (slower) pure
Javascript variant. The addon is approximately 10x faster than the pure JS version.
There are no external dependencies.

## NPM Install

    npm install basalt

## Building

In the project directory enter:

    node-gyp configure

Then enter:

    node-gyp build

## Usage

The library automatically loads the addon variant if it is available:

    var bson = require('/path/to/lib/bson');

    bson.encode({foo: 'bar'});
    bson.decode(bson.encode({foo: 'bar'});

To force either the addon or the pure js version, simply require them explicitly:

    var bson_pure = require('/path/to/lib/bson_pure'),
        bson_ext  = require('/path/to/lib/bson_ext');

## Notes

Portions of the code have been nicked from various places including node-mongodb-native,
node-mongodb, and the mongo c driver, though the c/c++ code was rewritten to support
more robust error handling. Have a look at /test and /benchmarks for more details.

In my branch of node-mongodb-native I'm seeing a 5-7x increase in performance
with the addon variant.

## Compilation/Build Notes

Currently, this library only builds reliably on Win32.

A Linux build is in the works, and potentially a Mac build as well.