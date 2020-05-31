# BananoPy

BananoPy is an all in one library for communicating with Banano/Nano nodes.

BananoPy contains nearly every single RPC call on https://docs.nano.org in the form of a simple python function call making it easy for anyone to make the most out of their node.
Rather than handling lots of JSON formatting, remembering what call accepts which perameters, all parameters are handled in the form of Python parameters and where possible, responses are parsed for you into a variable or object.

Example: `blockinfo = banano.get_block_count()` will return all the current block information in an object.
To then access the data such as block count it can be called simply as `blockinfo.count`

This library was written with node version 18 in mind. Some functions will work with later node versions however some might require extra parameters.

Pull requests are welcome as due to the number of functions written (100+), not all have been tested fully.

For more information on each function, please visit https://docs.nano.org/commands/rpc-protocol/

**Ref:** Initial version from BananoPy `repo <https://github.com/Kirby1997/BananoPy>`_.
