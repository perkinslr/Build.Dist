pipeline
{
	agent any
	stages
	{
		stage('Build')
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
			}
			environment
			{
				PROJECT="GenPi64${INIT_SYSTEM}$FLAVOR}"
			}
			steps
			{
				./build.sh
			}
		}
	}
}
