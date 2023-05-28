


swig  -c++ -python example.i

rm -rf build
rm -rf example.egg*

python3 setup.py install