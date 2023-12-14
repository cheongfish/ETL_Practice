import click
from pipeline import controller
from datetime import datetime


#########################################################################################################

@click.command
@click.option('-d','--batch-date', type = click.STRING, default = '')
def start_batch(batch_date):
    
    print("batch process start")
    
    if batch_date:
        _date = batch_date
        
    else:
        _date = datetime.now().strftime("%Y%m%d")
        
    controller.main(_date)
    
    print("batch process end")
    
    
    
start_batch()
    
    