spack stack for encfs


# Build

Stack must be built on a compute node (mandatory when rocm or cuda is used)
```
salloc -t 400 -p cpu
srun --pty bash
```

```bash
cd /dev/shm
git clone https://github.com/eth-cscs/stackinator.git
cd stackinator
./bootstraph.sh
bin/stack-config --develop -b /dev/shm//build-bwrap -s ~/stacks/alps-cluster-config/hohgant/ -r ~/encfs-stackinator -c /scratch/e1000/$(whoami)/cache-config.yaml
```
Then run the commands printed by stack-config.

Note:
- `alps-cluster-config`: https://github.com/eth-cscs/alps-cluster-config


__Wipe `/dev/shm` before releasing the slurm allocation__
