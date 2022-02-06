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
			}
			stages { stage('Build')
			{
				steps
				{
					sh "./build.sh"
				}
			}}
		}
	}}
}
