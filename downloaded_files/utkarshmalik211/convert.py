im = Image.open("input.jpg")
a = rescale(im)
a = Variable(a)
a = netG(a.view(-1, 3, 128, 128))
vutils.save_image(a.data, 'result.png', normalize=True)
