from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt


fc=10 # Р§Р°СЃС‚РѕС‚Р° РєРѕСЃРёРЅСѓСЃР° 
fs=32*fc # С‡Р°СЃС‚РѕС‚Р° РґРёСЃРєСЂРµС‚РёР·Р°С†РёРё, РёР·Р±С‹С‚РѕС‡РЅР°СЏ 
t=np.arange( 0, 2,  1/fs) # РґР»РёС‚РµР»СЊРЅРѕСЃС‚СЊ СЃРёРіРЅР°Р»Р° 2 СЃ
x=np.cos(2*np.pi*fc*t) # С„РѕСЂРјРёСЂРѕРІР°РЅРёРµ РІСЂРµРјРµРЅРЅРѕРіРѕ СЃРёРіРЅР°Р»Р°
plt.figure(1)
plt.plot(t,x) 
#plt.stem(t,x) # РґР»СЏ РѕС‚РѕР±СЂР°Р¶РµРЅРёСЏ РІСЂРµРјРµРЅРЅС‹С… РѕС‚СЃС‡РµС‚РѕРІ СЃРёРіРЅР°Р»Р°, РІС‹Р±СЂР°С‚СЊ РґР»РёС‚РµР»СЊРЅРѕСЃС‚СЊ 0.2 СЃРµРє
plt.xlabel('$t=nT_s$')
plt.ylabel('$x[n]$') 
N=256 # РєРѕР»РёС‡РµСЃС‚РІРѕ С‚РѕС‡РµРє Р”РџР¤
X = fft(x,N)/N # РІС‹С‡РёСЃР»РµРЅРёРµ Р”РџР¤ Рё РЅРѕСЂРјРёСЂРѕРІР°РЅРёРµ РЅР° N
plt.figure(2)
k = np.arange(0, N)
plt.stem(k,abs(X)) # РІС‹РІРѕРґРёРј РјРѕРґСѓР»СЊ Р”РџР¤ РІ С‚РѕС‡РєР°С… Р”РџР¤
plt.xlabel('k')
plt.ylabel('$x[k]$') 

df=fs/N
kf = k*df
plt.figure(3)
plt.stem(kf,abs(X)) # РІС‹РІРѕРґРёРј РјРѕРґСѓР»СЊ Р”РџР¤ РІ С‡Р°СЃС‚РѕС‚Р°С… 
plt.xlabel('Р“С†')
plt.ylabel('$x[k]$') 


k2 = np.arange(-N/2, N/2)
kf2=k2*df
X2 = fftshift(X) # СЃРґРІРёРі Р”РџР¤ РЅР° С†РµРЅС‚СЂ 
plt.figure(4)
plt.stem(kf2,abs(X2))
plt.xlabel('Р“С†')
plt.ylabel('$x[k]$') 


plt.figure(5)
x_ifft = N*ifft(X,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # РІСЂРµРјРµРЅРЅС‹Рµ РѕС‚СЃС‡РµС‚С‹ РєРѕР»РµР±Р°РЅРёСЏ
plt.xlabel('c')
plt.ylabel('$x[n]$') 