library(ggplot2)
library(ggpmisc)
library(tidyverse)
library(vioplot)
library(patchwork)
library(openxlsx)
set.seed(1234)

#麦芽糖
x = c(0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0)
y = c(0, 0.090, 0.353, 0.669, 0.936, 1.173, 1.234)
df = data.frame(x)
df$y = y

my.formula <- y ~ x
p <- ggplot(data = df, aes(x = x, y = y)) +
  geom_smooth(method = "lm", se=FALSE, color="black", formula = my.formula) +
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE) +         
  geom_point() +
  labs(x = "麦芽糖含量(mL)") + ylab(bquote(吸光度A[540]))



dianfen0 = c(0.161, 0.128) / 0.48
dianfen50 = c(0.203, 0.214) / 0.54
dianfen100 = c(0.240, 0.256) / 0.49
t.test(dianfen0, dianfen50, paired = F)
t.test(dianfen0, dianfen100, paired = F)


rootdf = data.frame(x = c(1:10))
rootdf$ya0 = c(14.5,14.2,15.2,14.3,14.2,14.8,14.1,14.6,14.0,13.9)
rootdf$ya50 = c(8.7,8.6,8.9,10.0,10.1,9.2,9.9,10,9.8,8.8)
rootdf$ya100 = c(11.6,10.1,6.7,7.0,7.7,9.4,8.2,8.1,9.0,9.5)

t.test(rootdf$ya0, rootdf$ya50)
t.test(rootdf$ya0, rootdf$ya100)
t.test(rootdf$ya50, rootdf$ya100)

rootdf$root0 = c(25.5,24.2,26.2,25.2,27.0,24.5,24.6,24.8,25.4,26.1)
rootdf$root50 = c(16.0,21.2,19.4,20.4,24.0,23.1,23.5,21.2,17.5,18.8)
rootdf$root100 = c(21.1,23.7,18.1,18.2,14.7,23.8,19.4,23.5,21.1,20.5)
  
rootdf$num0 = c(12,12,11,10,11,13,9,12,10,14)
rootdf$num50 = c(6,6,7,6,6,8,6,5,6,4)
rootdf$num100 = c(7,5,5,7,4,6,6,5,5,5)


mean_ya0 = mean(rootdf$ya0)
mean_ya50 = mean(rootdf$ya50)
mean_ya100 = mean(rootdf$ya100)
sd_ya0 = sd(rootdf$ya0)
sd_ya50 = sd(rootdf$ya50)
sd_ya100 = sd(rootdf$ya100)

ya_sd = c(sd_ya0, sd_ya50, sd_ya100)
ya_mean = c(mean_ya0, mean_ya50, mean_ya100)
ya_lab = c("0","50","100")

yadf = data.frame(x=ya_lab, y=ya_mean)
buds = ggplot(data = yadf, mapping=aes(x = x, y = y)) + 
      geom_bar(stat = 'identity', width = 0.5) + 
  geom_errorbar(aes(ymin = ya_mean - ya_sd), ymax = ya_mean + ya_sd,color = "#22292F",width = .1) +
  scale_fill_grey(start = 1, end = 0) + theme_minimal() +
  labs(x = "多效唑浓度mg/mL",y = "芽长(cm)")


p_value_one <- tibble(
  x = c("0","0","50","50"),
  y = c(17.5, 18, 18, 17.5))

p_value_two <- tibble(
  x = c("100","100","50","50"),
  y = c(11.5, 12, 12, 11.5))

p_value_three <- tibble(
  x = c("0","0","100","100"),
  y = c(15.5, 16, 16, 15.5))

buds = buds + geom_line(data = p_value_one, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_two, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_three, aes(x = x, y = y, group = 1)) +
  annotate("text", x = 2, y = 18.5, label = "**",size = 8, color = "#22292F") +
  annotate("text", x = 2.5, y = 13, label = "ns",size = 6, color = "#22292F") +
  annotate("text", x = 1.5, y = 16.5, label = "***",size = 8, color = "#22292F")

#roots
mean_rt0 = mean(rootdf$root0)
mean_rt50 = mean(rootdf$root50)
mean_rt100 = mean(rootdf$root100)
sd_rt0 = sd(rootdf$root0)
sd_rt50 = sd(rootdf$root50)
sd_rt100 = sd(rootdf$root100)
rt_sd = c(sd_rt0, sd_rt50, sd_rt100)
rt_mean = c(mean_rt0, mean_rt50, mean_rt100)
rt_lab = c("0","50","100")

rtdf = data.frame(x=rt_lab, y=rt_mean)
roots = ggplot(data = rtdf, mapping=aes(x = x, y = y)) + 
  geom_bar(stat = 'identity', width = 0.5) + 
  geom_errorbar(aes(ymin = rt_mean - rt_sd), ymax = rt_mean + rt_sd,color = "#22292F",width = .1) +
  scale_fill_grey(start = 1, end = 0) + theme_minimal() +
  scale_y_continuous(limits = c(0, 35), expand = c(0, 0)) + 
  labs(x = "多效唑浓度mg/mL",y = "根长(cm)")

p_value_one <- tibble(
    x = c("0","0","50","50"),
    y = c(30, 30.5, 30.5, 30))
  
p_value_two <- tibble(
    x = c("100","100","50","50"),
    y = c(24.5, 25, 25, 24.5))
  
p_value_three <- tibble(
    x = c("0","0","100","100"),
    y = c(27.5, 28, 28, 27.5))

roots = roots + geom_line(data = p_value_one, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_two, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_three, aes(x = x, y = y, group = 1)) +
  annotate("text", x = 2, y = 31, label = "***",size = 8, color = "#22292F") +
  annotate("text", x = 2.5, y = 26, label = "ns",size = 6, color = "#22292F") +
  annotate("text", x = 1.5, y = 28.5, label = "***",size = 8, color = "#22292F")

#nums
mean_nu0 = mean(rootdf$num0)
mean_nu50 = mean(rootdf$num50)
mean_nu100 = mean(rootdf$num100)

sd_nu0 = sd(rootdf$num0)
sd_nu50 = sd(rootdf$num50)
sd_nu100 = sd(rootdf$num100)
nu_sd = c(sd_nu0, sd_nu50, sd_nu100)
nu_mean = c(mean_nu0, mean_nu50, mean_nu100)
nu_lab = c("0","50","100")

nudf = data.frame(x=nu_lab, y=nu_mean)
nums = ggplot(data = nudf, mapping=aes(x = x, y = y)) + 
  geom_bar(stat = 'identity', width = 0.5) + 
  geom_errorbar(aes(ymin = nu_mean - nu_sd), ymax = nu_mean + nu_sd,color = "#22292F",width = .1) +
  scale_fill_grey(start = 1, end = 0) + theme_minimal() +
  labs(x = "多效唑浓度mg/mL",y = "根数(个)")
nums

p_value_one <- tibble(
  x = c("0","0","50","50"),
  y = c(16, 16.5, 16.5, 16))

p_value_two <- tibble(
  x = c("100","100","50","50"),
  y = c(8, 8.5, 8.5, 8))

p_value_three <- tibble(
  x = c("0","0","100","100"),
  y = c(14, 14.5, 14.5, 14))

nums = nums + geom_line(data = p_value_one, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_two, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_three, aes(x = x, y = y, group = 1)) +
  annotate("text", x = 2, y = 17, label = "***",size = 8, color = "#22292F") +
  annotate("text", x = 2.5, y = 9, label = "ns",size = 6, color = "#22292F") +
  annotate("text", x = 1.5, y = 15, label = "***",size = 8, color = "#22292F")

nums

#vio
attach(mtcars)
opar<-par(no.readonly=T)
par(mfrow=c(1,3))
vio.ya = vioplot(rootdf$ya0, rootdf$ya50, rootdf$ya100, names = c('buds-0', 'buds-50', 'buds-100'))
vio.rt = vioplot(rootdf$root0, rootdf$root50, rootdf$root100,names = c('root-0', 'root-50', 'root-100'))
vio.nu = vioplot(rootdf$num0, rootdf$num50, rootdf$num100,names = c('rnum-0', 'rnum-50', 'rnum-100'))
par(opar)
detach(mtcars)

#bar
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}


plot_list <- list(buds,roots, nums)
multiplot(plotlist = plot_list, cols = 3)

#丙二醛
bingdf = read.xlsx("bing.xlsx",sheet=1)
bingdf$absorb = c("A450", "A532", "A600")
ggplot(bingdf, aes(fill=absorb)) + 
  geom_line(data = bingdf, aes(x = X1, y = A450), color='blue') +
  geom_line(data = bingdf, aes(x = X1, y = A532), color='#FF3333') +
  geom_line(data = bingdf, aes(x = X1, y = A600), color="#00CC33") +
  labs(x = "多效唑浓度mg/mL",y = "吸光度")
  

#脯氨酸
x = c(0, 2, 4, 6, 8, 12, 16, 20)
y = c(0.003, 0.062, 0.113, 0.179, 0.233, 0.343, 0.475, 0.577)
df = data.frame(x)
df$y = y

my.formula <- y ~ x
p <- ggplot(data = df, aes(x = x, y = y)) +
  geom_smooth(method = "lm", se=FALSE, color="black", formula = my.formula) +
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE) +         
  geom_point() +
  labs(x = "脯氨酸浓度(μg/mL)") + ylab(bquote(吸光度A[515]))
p

