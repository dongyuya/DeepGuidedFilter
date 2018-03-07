from torch.autograd import Variable

from module import DeepGuidedFilter

from test_base import *

default_config.NAME = 'HR_NO_TRAINING'
default_config.SET_NAME = 1024

# model
model = DeepGuidedFilter()
model.init_lr(os.path.join(default_config.MODEL_PATH, default_config.TASK,
                           'LR', 'snapshots', 'net_latest.pth'))
default_config.model = model

# forward
def forward(imgs, config):
    lr_x, hr_x = imgs[2].unsqueeze(0), imgs[0].unsqueeze(0)
    if config.GPU >= 0:
        with torch.cuda.device(config.GPU):
            lr_x = lr_x.cuda()
            hr_x = hr_x.cuda()

    return config.model(Variable(lr_x), Variable(hr_x)).data.cpu()
default_config.forward = forward

run(default_config)
