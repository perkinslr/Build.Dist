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
			}
			environment
			{
				PROJECT="GenPi64${INIT_SYSTEM}${FLAVOR}"
			}
			stages { stage('Build')
			{
				steps
				{
					sh "ls -lahR"
					sh "build.sh"
				}
			}}
		}
	}}
}
