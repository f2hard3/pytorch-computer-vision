import torchvision
import torchvision.transforms as tr
from torch.utils.data import DataLoader

def dataloader(batch_size, train_mode):
    transform = tr.Compose([
        tr.RandomCrop(32, padding=4),
        tr.RandomHorizontalFlip(),
        tr.ToTensor(),
        tr.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])
    test_transform = tr.Compose([
        tr.ToTensor(),
        tr.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])    
    trainset = torchvision.datasets.CIFAR10(
        root='data', download=True, train=True, 
        transform=transform if train_mode == 'train' else test_transform
    )
    trainloader = DataLoader(trainset, batch_size=batch_size, num_workers=0)
    
    testset = torchvision.datasets.CIFAR10(
        root='data', download=True, train=False, transform=test_transform
    )
    testloader = DataLoader(testset, batch_size=batch_size, num_workers=0)

    return trainloader, testloader