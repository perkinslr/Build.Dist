pipeline
{
	agent none
	stages { stage('Build')
	{
		matrix
		{
			agent any
			axes
			{
				axis
				{
					name 'INIT_SYSTEM'
					values 'OpenRC', 'Systemd'
				}
				axis
				{
					name 'FLAVOR'
					values '', 'Desktop'
				}
				axis
				{
					name 'LIBC'
					values 'GlibC'
				}
				axis
				{
					name 'PartitionScheme'
					values 'MsDos'
				}
				axis
				{
					name 'Arch'
					values 'aarch64'
				}
			}
			environment
			{
				PROJECT="GenPi64${INIT_SYSTEM}${FLAVOR}"
				NO_PARALLEL="yes"
				CHROOT_COMMAND="systemd-nspawn"
			}
			stages { stage('Build')
			{
				steps
				{
					sh "sudo ./build.sh"
				}
			}}
		}
	}}
}
