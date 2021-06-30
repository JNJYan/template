# build

```shell
mkdir build && cd build
conan install .. -u --build=missing -r=conancenter 
cmake .. && make -j 8
# -u: if package version is in range, will be updated to new version if remote repo existing.
# --build=missing: the profile don't match the compile setup of package, download source and recompile it.
# -r: assign the remote repo
```